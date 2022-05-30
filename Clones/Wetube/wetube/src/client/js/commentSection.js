const videoContainer = document.getElementById("videoContainer");

const form = document.getElementById("commentForm");

const handleSubmit = () => {
  event.preventDefault();

  const textarea = form.querySelector("textarea");

  const text = textarea.value;
  const videoId = videoContainer.dataset.id;

  if (text === "") {
    return;
  }

  fetch(`/api/videos/${videoId}/comment`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  textarea.value = "";
};

if (form) {
  form.addEventListener("submit", handleSubmit);
}
