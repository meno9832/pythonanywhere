document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.nav-link');
    const ajaxContent = document.getElementById('ajax-content');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.getAttribute('href');

            fetch(url)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.text();
                })
                .then(data => {
                    ajaxContent.innerHTML = data;
                })
                .catch(error => console.error('Error:', error));
        });
    });

    // 기본 콘텐츠 URL 설정 (적절한 파일 경로로 수정)
    const defaultUrl = '/main'; // 기본 콘텐츠 URL
    fetch(defaultUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            ajaxContent.innerHTML = data;
        })
        .catch(error => console.error('Error loading default content:', error));
});
// ajax.js
function loadContent(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById('ajax-content').innerHTML = data;
            
            // AJAX로 로드된 콘텐츠에 대해 추가적인 스타일 적용
            document.getElementById('ajax-content').style.color = 'blue'; // 예시
        })
        .catch(error => console.error('Error loading content:', error));
}