function resizeIframe(e) {
  var body = document.body,
  html = document.documentElement;

  var height = Math.max( body.scrollHeight, body.offsetHeight, 
                     html.clientHeight, html.scrollHeight, html.offsetHeight );
  console.log("resize :"+height );
  height *=1.1;
  //html.height = height+"px";
  window.parent.postMessage([height,window.location.href], "*"); 
}
window.onload = resizeIframe;