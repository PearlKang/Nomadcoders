const video = document.querySelector("video");
const playBtn = document.getElementById("play");
const muteBtn = document.getElementById("mute");
const time = document.getElementById("time");
const volumeRange = document.getElementById("volume");

let volumeValue = 0.5;
video.volume = volumeValue;

const handelPlayClick = (e) => {
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
  playBtn.innerText = video.paused ? "Play" : "Pause";
};

const handelMuteClick = (e) => {
  if (video.muted) {
    video.muted = false;
  } else {
    video.muted = true;
  }
  muteBtn.innerText = video.muted ? "Unmute" : "Mute";
  volumeRange.value = video.muted ? 0 : volumeValue;
};

const handleVolumeChange = (event) => {
  const {
    target: { value },
  } = event;

  volumeValue = value;
  video.volume = value;

  if (video.muted) {
    video.muted = false;
    muteBtn.innerText = "Mute";
  }

  if (volumeValue === "0") {
    video.muted = true;
    muteBtn.innerText = "Unmute";
  }
};

playBtn.addEventListener("click", handelPlayClick);
muteBtn.addEventListener("click", handelMuteClick);
volumeRange.addEventListener("input", handleVolumeChange);
