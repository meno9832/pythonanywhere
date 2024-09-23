/*갤러리용*/
function openModal(element) {
    var modal = document.getElementById('modal');
    var modalImage = document.getElementById('modal-image');
    
    // 이미지 태그에서 src 속성 추출
    var url = element.src;

    modalImage.src = url;
    modal.style.display = 'flex'; // 모달 창 표시
}


function closeModal(event) {
    var modal = document.getElementById('modal');

    // 클릭한 요소가 모달 바깥인지 확인
    if (event.target === modal) {
        modal.style.display = 'none'; // 모달 창 숨김
    }
}


// 필터링 기능
function filterGallery(category) {
    var items = document.querySelectorAll('.gallery-item');
    
    items.forEach(function(item) {
        if (category === 'all' || item.classList.contains(category)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}
function filterCards(category) {
    var cards = document.getElementsByClassName('cardLink');

    for (var i = 0; i < cards.length; i++) {
        if (category === 'all' || cards[i].classList.contains(category)) {
            cards[i].style.display = 'block'; // 선택한 카테고리의 카드 보이기
        } else {
            cards[i].style.display = 'none'; // 선택하지 않은 카테고리의 카드 숨기기
        }
    }
}

function filterCaracter(category) {
    const cards = document.querySelectorAll('.character-card');

    cards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');

        if (category === 'all' || cardCategory === category) {
            card.style.display = 'block'; // 카드 표시
        } else {
            card.style.display = 'none'; // 카드 숨기기
        }
    });
}