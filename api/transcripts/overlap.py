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