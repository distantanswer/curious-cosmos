from flask import Flask, request, jsonify, Response
from transcript_analyzer import fetch_transcript, find_common_chunks
import json

app = Flask(__name__)

@app.route('/api/')
def hello_world():
    return 'Hello, world!', 200, {'Content-Type': 'text/plain'}

def stream_common_chunks(video_ids):
    for chunk in find_common_chunks(video_ids):
        yield f"data: {json.dumps(chunk)}\n\n"

@app.route('/api/transcripts/common')
def compare_transcripts_stream():
    video_ids = request.args.getlist('videoIds')
    print(video_ids)
    if len(video_ids) != 2:
        return jsonify({"message":"Only supports exactly two ids"}), 400

    # returns a dict of { video_id: transcript_chunks }
    transcripts = fetch_transcript(video_ids)
    print("Successfully fetched transcripts")
    
    return Response(stream_common_chunks(transcripts), content_type='text/event-stream')

@app.route('/api/transcripts/overlap')
def check_transcripts_overlap():
    video_ids = request.args.getlist('videoIds')
    if len(video_ids) != 2:
        return jsonify({"message":"Only supports exactly two ids"}), 400

    transcripts = fetch_transcript(video_ids)
    identical_chunk_count = 0
    for chunk in find_common_chunks(transcripts, True):
        identical_chunk_count += 1

    shorter_video_total_chunks = min(len(transcripts[video_ids[0]]), len(transcripts[video_ids[1]]))
    amount_overlap = identical_chunk_count / shorter_video_total_chunks
    print(shorter_video_total_chunks)
    print(identical_chunk_count)
    return jsonify({"overlap": amount_overlap}), 200
# If using Vercel, you need to expose the `app` object as `app` for it to recognize it.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

