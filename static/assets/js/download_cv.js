
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'assets/cv_resume.pdf'; // Ensure this path is correct
    link.download = 'cv_resume.pdf'; // Set the filename for download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}