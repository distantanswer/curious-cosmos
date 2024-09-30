import { useEffect, useRef, useState } from 'react';

function YoutubeEmbed({embedId, timestamp}) {
  const playerRef = useRef(null);
  const [player, setPlayer] = useState(null);
console.log(embedId);
  console.log(timestamp);
  useEffect(() => {
    console.log('useEffect', window.YT);
    if (window.YT && window.YT.Player) {
      const newPlayer = new window.YT.Player(playerRef.current, {
        height: '390',
        width: '640',
        videoId: embedId,
        events: {
          onReady: (event) => {
            console.log("Player is ready!");
          },
        },
      });
      setPlayer(newPlayer);
    }else{
      console.error('YT api or Player not available')
    }
  }, [embedId]);

  useEffect(() => {
   if(player && timestamp){
      player.seekTo(timestamp, true)
    }else{
     console.error('no player to seek to')
    }
  }, [timestamp])

  return (
    <div>
      <h1>My YouTube Player</h1>
      <div ref={playerRef}></div>
    </div>
  );
}

export default YoutubeEmbed;

