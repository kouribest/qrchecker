function fillUp(target, content){
  $('.'+target).append(content)
}
let scanner = new Instascan.Scanner({ 
  video: document.getElementById('preview'),
   });
      scanner.addListener('scan', function (content) {
        fillUp('scan-list', '<a href="/admin/mali_project/formmodel/YPAWVZ/change/"'+content+'/change>'+content+'</a>')
      });
      Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
          for (var x in cameras){
           fillUp('cam-list', cameras[x].name)// we show up all available cameras
          }
          scanner.start(cameras[0]); // we start the first by default
        } else {
          fillUp('cam-list', 'No cameras found.'); // else  show an error message
        }
      }).catch(function (e) {
        console.error(e);
    });