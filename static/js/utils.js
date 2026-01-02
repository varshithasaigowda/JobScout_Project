function showPopup(message, type = "info") {
    const popup = document.createElement("div");
    popup.className = `popup ${type}`;
    popup.innerText = message;

    document.body.appendChild(popup);

    setTimeout(() => popup.classList.add("visible"), 100);
    setTimeout(() => popup.remove(), 3000);
}

function statusColor(status) {
    if (status === "ACCEPTED") return "green";
    if (status === "REJECTED") return "red";
    if (status === "HOLD") return "orange";
    return "gray";
}
