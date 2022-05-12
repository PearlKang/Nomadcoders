const video = document.querySelector("video");
const playBtn = document.getElementById("play");
const muteBtn = document.getElementById("mute");
const time = document.getElementById("time");
const volume = document.getElementById("volume");

const handelPlayClick = (e) => {
  // if the video is playing, pause it
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
  // else play the video.
};

const handelPause = () => (playBtn.innerText = "Play");
const handelPlay = () => (playBtn.innerText = "Pause");

const handelMute = (e) => {};

playBtn.addEventListener("click", handelPlayClick);
muteBtn.addEventListener("click", handelMute);
video.addEventListener("pause", handelPause);
video.addEventListener("play", handelPlay);
