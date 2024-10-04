import { useState } from 'react'; // Import useState hook
import './App.css';
import YoutubeEmbed from "./components/YoutubeEmbed.js"; // Import the YoutubeEmbed component

function App() {
  // Use state to store the video URLs
  const [firstVideoUrl, setFirstVideoUrl] = useState("");
  const [secondVideoUrl, setSecondVideoUrl] = useState("");
  const [firstVideoTimestamp, setFirstVideoTimestamp] = useState(0.00);


  // Function to extract the video ID from a full YouTube URL
  const extractVideoId = (url) => {
    const regex = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^/\n\s]+\/\S+\/|(?:v|embed|shorts)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
    const match = url.match(regex);
    return match ? match[1] : "";
  };

  const setTimestamps = () => {
    setFirstVideoTimestamp(100);
  }

  return (
    <div className="App">
      <h1>Add your YouTube video URLs!</h1>
      
      {/* First Input */}
      <input
        type="text"
        placeholder="Enter first YouTube video URL"
        onChange={(e) => setFirstVideoUrl(extractVideoId(e.target.value))}
      />
      
      {/* Second Input */}
      <input
        type="text"
        placeholder="Enter second YouTube video URL"
        onChange={(e) => setSecondVideoUrl(extractVideoId(e.target.value))}
      />
      
      {/* Embed components for both videos */}
      <div className="video-container">
        <YoutubeEmbed embedId={firstVideoUrl} timestamp={firstVideoTimestamp} />
        <YoutubeEmbed embedId={secondVideoUrl} />
      </div>

      <button onClick={setTimestamps}>Set Time</button>
    </div>
  );
}

export default App;

