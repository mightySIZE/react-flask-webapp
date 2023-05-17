// Load this script after the document is loaded
// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get all the elements with the "btn-close" class
    var closeButtons = document.querySelectorAll(".btn-close");

    // Attach a click event listener to each close button
    closeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            // Find the closest parent element with the "alert" class and remove it
            var alert = button.closest(".alert");
            if (alert) {
                alert.remove();
            }
        });
    });
});
