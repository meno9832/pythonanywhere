/*이미지 슬라이드*/
document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelector('.slides');
    const slideImages = document.querySelectorAll('.slide');
    
    // 이미지가 있는지 확인
    if (slideImages.length === 0) {
        console.error('슬라이드 이미지가 로드되지 않았습니다.');
        return;  // 슬라이드 이미지가 없으면 중단
    }
    
    let index = 0;

    function showSlide(idx) {
        const slideWidth = slideImages[0].clientWidth; // 슬라이드의 너비를 가져옴
        slides.style.transform = `translateX(${-idx * slideWidth}px)`; // 슬라이드 크기만큼 이동
    }

    function showNextSlide() {
        index++;
        if (index >= slideImages.length) {
            index = 0;
        }
        console.log('슬라이드 이동:', index);
        showSlide(index);
    }

    function showPrevSlide() {
        index--;
        if (index < 0) {
            index = slideImages.length - 1;
        }
        showSlide(index);
    }

    // 5초마다 자동 슬라이드
    setInterval(showNextSlide, 5000);

    // 버튼 클릭 이벤트
    document.querySelector('.next-btn').addEventListener('click', showNextSlide);
    document.querySelector('.prev-btn').addEventListener('click', showPrevSlide);
});



/*시계*/
function displayClock() {
    const clockTarget = document.getElementById("clock");
    if (!clockTarget) return; // 요소가 없으면 종료

    const date = new Date();
    const month = date.getMonth() + 1; // 0부터 시작하므로 +1
    const clockDate = date.getDate();
    const day = date.getDay();
    const week = ['일', '월', '화', '수', '목', '금', '토'];
    const hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();

    clockTarget.innerText = `${month}월 ${clockDate}일 ${week[day]}요일
    ${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}:${seconds < 10 ? `0${seconds}` : seconds}`;
}

function init() {
    displayClock();
    setInterval(displayClock, 1000);
}

init();



/*배너 복사*/
function copyToClipboard() {
    // 복사할 주소 (여기서는 예시로 배너 이미지 주소를 설정)
    const bannerUrl = 'https://i.imgur.com/0qIxdoE.png';

    // 클립보드에 텍스트 복사
    navigator.clipboard.writeText(bannerUrl)
        .then(() => {
            // 복사가 성공하면 알림 메시지 표시
            const alertMessage = document.getElementById('alert-message');
            alertMessage.style.display = 'block';
            
            // 3초 후에 알림 메시지를 숨김
            setTimeout(() => {
                alertMessage.style.display = 'none';
            }, 3000);
        })
        .catch(err => {
            console.error('복사 실패: ', err);
        });
}