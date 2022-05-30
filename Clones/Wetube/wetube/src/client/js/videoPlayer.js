const video = document.querySelector("video");
const playBtn = document.getElementById("play");
const playBtnIcon = playBtn.querySelector("i");
const muteBtn = document.getElementById("mute");
const muteBtnIcon = muteBtn.querySelector("i");
const volumeRange = document.getElementById("volume");
const currentTime = document.getElementById("currentTime");
const totalTime = document.getElementById("totalTime");
const timeline = document.getElementById("timeline");
const fullScreenBtn = document.getElementById("fullScreen");
const fullScreenIcon = fullScreenBtn.querySelector("i");
const videoContainer = document.getElementById("videoContainer");
const videoControls = document.getElementById("videoControls");

let controlsTimeout = null;
let controlsMovementTimeout = null;
let volumeValue = 0.5;
video.volume = volumeValue;

const handlePlayClick = (e) => {
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }

  playBtnIcon.classList = video.paused ? "fas fa-play" : "fas fa-pause";
};

const handleMuteClick = (e) => {
  if (video.muted) {
    video.muted = false;
  } else {
    video.muted = true;
  }

  muteBtnIcon.classList = video.muted
    ? "fas fa-volume-mute"
    : "fas fa-volume-up";

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
    muteBtnIcon.classList = "fas fa-volume-up";
  }

  if (value === "0") {
    video.muted = true;
    muteBtnIcon.classList = "fas fa-volume-mute";
  }
};

const formatTime = (seconds) => {
  const idx = seconds >= 3600 ? 11 : 14;

  return new Date(seconds * 1000).toISOString().substring(idx, 19);
};

const handleLoadedMetadata = () => {
  totalTime.innerText = formatTime(Math.floor(video.duration));
  timeline.max = Math.floor(video.duration);
};

const handleTimeUpdate = () => {
  currentTime.innerText = formatTime(Math.floor(video.currentTime));
  timeline.value = Math.floor(video.currentTime);
};

const handleTimelineChange = (event) => {
  const {
    target: { value },
  } = event;

  video.currentTime = value;
};

const handleFullscreen = () => {
  const fullscreen = document.fullscreenElement;

  if (fullscreen) {
    document.exitFullscreen();
    fullScreenIcon.classList = "fas fa-expand";
  } else {
    videoContainer.requestFullscreen();
    fullScreenIcon.classList = "fas fa-compress";
  }
};

const hideControls = () => videoControls.classList.remove("showing");

const handleMouseMove = () => {
  if (controlsTimeout) {
    clearTimeout(controlsTimeout);
    controlsTimeout = null;
  }

  if (controlsMovementTimeout) {
    clearTimeout(controlsMovementTimeout);
    controlsMovementTimeout = null;
  }

  videoControls.classList.add("showing");

  controlsMovementTimeout = setTimeout(hideControls, 3000);
};

const handleMouseLeave = () => {
  controlsTimeout = setTimeout(hideControls, 3000);
};

const handleKeydown = (event) => {
  const { keyCode } = event;

  //event.preventDefault();

  switch (keyCode) {
    case 32:
      handlePlayClick();
      break;
    case 13:
      //case 70:
      //case 102:
      handleFullscreen();
      break;
    //case 77:
    //case 109:
    //  handleMuteClick();
    //  break;
    //case 37:
    //  video.currentTime = video.currentTime < 5 ? 0 : video.currentTime - 5;
    //  break;
    //case 38:
    //  video.volume = video.volume >= 1 ? 1 : video.volume + 0.1;
    //  if (video.muted) {
    //    video.muted = false;
    //    muteBtnIcon.classList = "fas fa-volume-up";
    //  }
    //  break;
    //case 39:
    //  video.currentTime =
    //    video.currentTime > video.duration ? 0 : video.currentTime + 5;
    //  break;
    //case 40:
    //  video.volume = video.volume >= 0 ? 0 : video.volume - 0.1;
    //  if (video.muted) {
    //    video.muted = true;
    //    muteBtnIcon.classList = "fas fa-volume-mute";
    //  }
    //  break;
  }
};

const handleEnded = () => {
  const { id } = videoContainer.dataset;

  fetch(`/api/videos/${id}/view`, {
    method: "POST",
  });
};

playBtn.addEventListener("click", handlePlayClick);
muteBtn.addEventListener("click", handleMuteClick);
volumeRange.addEventListener("input", handleVolumeChange);
video.addEventListener("loadedmetadata", handleLoadedMetadata);
video.addEventListener("timeupdate", handleTimeUpdate);
video.addEventListener("ended", handleEnded);
videoContainer.addEventListener("mousemove", handleMouseMove);
videoContainer.addEventListener("mouseleave", handleMouseLeave);
timeline.addEventListener("input", handleTimelineChange);
fullScreenBtn.addEventListener("click", handleFullscreen);
video.addEventListener("click", handlePlayClick);
window.addEventListener("keydown", handleKeydown);
