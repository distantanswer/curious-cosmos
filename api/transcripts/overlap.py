from flask import jsonify
from transcript_analyzer import fetch_transcript, find_common_chunks
import json
from dotenv import load_dotenv
import os
load_dotenv()

has_yt_proxy = os.getenv("YT_TRANSCRIPT_PROXY_URL") != None

def handler(request):
    video_ids = request.args.getlist('videoIds')
    if len(video_ids) != 2:
        return jsonify({"message":"Only supports exactly two ids"}), 400

    print('INSIDE OVERLAP')
    print(video_ids)
    try:
        transcripts = fetch_transcript(video_ids)
        print(transcripts)
        if len(transcripts.keys()) < 2: raise Exception("Error getting transcripts")
    except:
        return jsonify({"message":"Error getting transcripts", "context": { "has_proxy": has_yt_proxy }}), 500

    identical_chunk_count = 0
    for chunk in find_common_chunks(transcripts, True):
        identical_chunk_count += 1

    shorter_video_total_chunks = min(len(transcripts[video_ids[0]]), len(transcripts[video_ids[1]]))
    amount_overlap = identical_chunk_count / shorter_video_total_chunks
    print(shorter_video_total_chunks)
    print(identical_chunk_count)
    return jsonify({"overlap": amount_overlap}), 200

