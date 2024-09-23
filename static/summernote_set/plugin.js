$(document).ready(function() {
  $('#summernote').summernote({
      height: 300,                 // 에디터 높이
      minHeight: null,             // 최소 높이
      maxHeight: null,             // 최대 높이
      focus: true,                 // 에디터 로딩 후 포커스를 맞출지 여부
      lang: "ko-KR",               // 한글 설정
      fontSizeUnits: 'px',
      dialogsInBody: true,
      disableDragAndDrop: true,

      toolbar: [
          // [groupName, [list of button]]
          ['style', ['style']],
          ['fontname', ['fontname']],
          ['fontsize', ['fontsize']],
          ['style', ['bold', 'italic', 'underline','strikethrough','superscript','subscript', 'clear']],
          ['color', ['forecolor','color']],
          ['table', ['table']],
          ['para', ['ul', 'ol', 'paragraph']],
          ['height', ['height']],
          ['insert',['picture','link','video']],
          ['view', ['fullscreen','codeview', 'help']],
      ],
      fontNames: ['Arial', 'Arial Black', 'Comic Sans MS', 'Courier New', 'Helvetica', 'Impact', 'Times New Roman','맑은 고딕','궁서','굴림체','굴림','돋움체','바탕체'],
      fontSizes: ['8','9','10','11','12','14','16','18','20','22','24','28','30','36','50','72'],
  });
});
