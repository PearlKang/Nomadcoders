const video = document.querySelector("video");
const playBtn = document.getElementById("play");
const muteBtn = document.getElementById("mute");
const time = document.getElementById("time");
const volume = document.getElementById("volume");

const handelPlay = (e) => {
  // if the video is playing, pause it
  if (video.paused) {
    playBtn.innerText = "Pause";
    video.play();
  } else {
    playBtn.innerText = "Play";
    video.pause();
  }
  // else play the video.
};

const handelMute = (e) => {};

playBtn.addEventListener("click", handelPlay);
muteBtn.addEventListener("click", handelMute);
