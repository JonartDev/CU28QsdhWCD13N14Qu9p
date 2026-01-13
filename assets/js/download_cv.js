
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'assets/JonartOlicia.pdf'; // Ensure this path is correct
    link.download = 'JonartOlicia.pdf'; // Set the filename for download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}