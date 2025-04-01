
// const pages = ["header","about", "education", "work", "footer"]; // List of HTML files to load

// async function loadAllPages() {
//     const contentDiv = document.getElementById("content");

//     for (let page of pages) {
//         try {
//             const response = await fetch(`source/${page}.html`);
//             const data = await response.text();
//             contentDiv.innerHTML += data; // Append content
//         } catch (error) {
//             console.error(`Error loading ${page}:`, error);
//         }
//     }
// }

// document.addEventListener("DOMContentLoaded", loadAllPages);