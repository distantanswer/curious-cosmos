from flask import jsonify, Response
from transcript_analyzer import fetch_transcript, find_common_chunks
import json

def stream_common_chunks(video_ids):
    for chunk in find_common_chunks(video_ids):
        yield f"data: {json.dumps(chunk)}\n\n"

def handler(request):
    video_ids = request.args.getlist('videoIds')
    print(video_ids)
    if len(video_ids) != 2:
        # Probably don't want to return json, when we normaly stream the response
        return jsonify({"message":"Only supports exactly two ids"}), 400

    # returns a dict of { video_id: transcript_chunks }
    transcripts = fetch_transcript(video_ids)
    print("Successfully fetched transcripts")
    
    return Response(stream_common_chunks(transcripts), content_type='text/event-stream')
