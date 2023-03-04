(self.webpackChunkopen3d=self.webpackChunkopen3d||[]).push([[261],{568:(e,t,n)=>{e.exports=n(34),e.exports.version=n(147).version},261:(e,t,n)=>{var o=n(568),i=n(337);e.exports={id:"open3d:plugin",requires:[i.IJupyterWidgetRegistry],activate:function(e,t){t.registerWidget({name:"open3d",version:o.version,exports:o})},autoStart:!0}},34:(e,t,n)=>{let o=n(337),i=n(431);n(171);let a=n(552),s=o.DOMWidgetModel.extend({defaults:i.extend(o.DOMWidgetModel.prototype.defaults(),{_model_name:"WebVisualizerModel",_view_name:"WebVisualizerView",_model_module:"open3d",_view_module:"open3d",_model_module_version:"0.16.0",_view_module_version:"0.16.0"})}),r=o.DOMWidgetView.extend({sleep:function(e){return new Promise((t=>setTimeout(t,e)))},logAndReturn:function(e){return console.log("logAndReturn: ",e),e},callResultReady:function(e){let t=this.model.get("pyjs_channel");return console.log("Current pyjs_channel:",t),e in JSON.parse(this.model.get("pyjs_channel"))},extractCallResult:function(e){if(!this.callResultReady(e))throw"extractCallResult not ready yet.";return JSON.parse(this.model.get("pyjs_channel"))[e]},callPython:async function(e,t=[]){let n=this.callId.toString();this.callId++;let o={func:e,args:t,call_id:n},i=this.model.get("jspy_channel"),a=JSON.parse(i);a[n]=o,i=JSON.stringify(a),this.model.set("jspy_channel",i),this.touch();let s=0;for(;!this.callResultReady(n);)console.log("callPython await, id: "+n+", count: "+s++),await this.sleep(100);let r=this.extractCallResult(n);return console.log("callPython await done, id:",n,"json_result:",r),r},commsCall:function(e,t={}){let n=function(e){let t=document.createElement("a");return t.href=e,t},o=n(e).pathname;if(["/api/getMediaList","/api/getIceServers","/api/hangup","/api/call","/api/getIceCandidate","/api/addIceCandidate"].indexOf(o)>=0){let i=n(e).search;i||(i="");let a=t.body;return a||(a=""),console.log("WebVisualizerView.commsCall with url: ",e," data: ",t),console.log("WebVisualizerView.commsCall with entryPoint: ",o),console.log("WebVisualizerView.commsCall with queryString: ",i),console.log('WebVisualizerView.commsCall with data["body"]: ',a),this.callPython("call_http_api",[o,i,a]).then((e=>JSON.parse(e))).then((e=>this.logAndReturn(e))).then((e=>new Response(new Blob([JSON.stringify(e)],{type:"application/json"})))).then((e=>this.logAndReturn(e)))}throw"Unsupported entryPoint: "+o},render:function(){let e=this.model.get("window_uid");console.log("Entered render() function."),this.model.set("pyjs_channel","{}"),this.model.set("jspy_channel","{}"),this.touch(),this.callId=0,this.videoElt=document.createElement("video"),this.videoElt.id="video_tag",this.videoElt.muted=!0,this.videoElt.controls=!1,this.videoElt.playsinline=!0,this.videoElt.innerText="Your browser does not support HTML5 video.",this.el.appendChild(this.videoElt),this.webRtcClient=new a(this.videoElt,"",(function(){console.log("onClose() called for window_uid:",e)}),this.commsCall.bind(this)),this.webRtcClient.connect(e)}});e.exports={WebVisualizerModel:s,WebVisualizerView:r}},552:e=>{void 0===window.console&&(window.console={}),window.console.log=window.console.info=window.console.debug=window.console.warning=window.console.assert=window.console.error=function(){};let t=function(){function e(e,t,n,o=null){this.videoElt="string"==typeof e?document.getElementById(e):e,this.srvurl=t||location.protocol+"//"+window.location.hostname+":"+window.location.port,this.pc=null,this.dataChannel=null,this.pcOptions={optional:[{DtlsSrtpKeyAgreement:!0}]},this.mediaConstraints={offerToReceiveAudio:!0,offerToReceiveVideo:!0},this.iceServers=null,this.earlyCandidates=[],this.onClose=n,this.commsFetch=o}return e.remoteCall=function(e,t={},n=null){return console.log("WebRtcStreamer.remoteCall{url: ",e,", data: ",t,", commsFetch",n,"}"),null==n?fetch(e,t):n(e,t)},e.getMediaList=function(t="",n=null){return e.remoteCall(t+"/api/getMediaList",{},n)},e._getModifiers=function(e){var t=2,n=8;window.navigator.platform.includes("Mac")&&([t,n]=[n,t]);var o=0;return e.getModifierState("Shift")&&(o|=1),e.getModifierState("Control")&&(o|=t),e.getModifierState("Alt")&&(o|=4),e.getModifierState("Meta")&&(o|=n),o},e.prototype._handleHttpErrors=function(e){if(!e.ok)throw Error(e.statusText);return e},e.prototype.connect=function(t,n,o,i){this.disconnect(),this.iceServers?this.onReceiveGetIceServers(this.iceServers,t,n,o,i):(console.log("Get IceServers"),e.remoteCall(this.srvurl+"/api/getIceServers",{},this.commsFetch).then(this._handleHttpErrors).then((e=>e.json())).then((e=>{return t=e,window.console.log("logAndReturn: ",t),t;var t})).then((e=>this.onReceiveGetIceServers.call(this,e,t,n,o,i))).catch((e=>this.onError("getIceServers "+e)))),this.addEventListeners(t)},e.prototype.sendJsonData=function(e){void 0!==this.dataChannel&&this.dataChannel.send(JSON.stringify(e))},e.prototype.addEventListeners=function(t){if(this.videoElt){this.videoElt.parentElement;var n=document.createElement("div"),o=document.createElement("input");o.id=t+"_height_input",o.type="text",o.value="",n.appendChild(o);var i=document.createElement("input");i.id=t+"_width_input",i.type="text",i.value="",n.appendChild(i);var a=document.createElement("button");a.id=t+"_resize_button",a.type="button",a.innerText="Resize",a.onclick=()=>{var e=document.getElementById(t+"_height_input"),n=document.getElementById(t+"_width_input");if(!e||!n)return void console.warn("Cannot resize, missing height/width inputs.");const o={window_uid:t,class_name:"ResizeEvent",height:parseInt(e.value),width:parseInt(n.value)};this.sendJsonData(o)},n.appendChild(a);var s=["LEFT","MIDDLE","RIGHT"];this.videoElt.addEventListener("contextmenu",(e=>{e.preventDefault()}),!1),this.videoElt.onloadedmetadata=function(){console.log("width is",this.videoWidth),console.log("height is",this.videoHeight);var e=document.getElementById(t+"_height_input");e&&(e.value=this.videoHeight);var n=document.getElementById(t+"_width_input");n&&(n.value=this.videoWidth)},this.videoElt.addEventListener("mousedown",(n=>{n.preventDefault();var o={window_uid:t,class_name:"MouseEvent",type:"BUTTON_DOWN",x:n.offsetX,y:n.offsetY,modifiers:e._getModifiers(n),button:{button:s[n.button],count:1}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("dblclick",(n=>{n.preventDefault();var o={window_uid:t,class_name:"MouseEvent",type:"BUTTON_DOWN",x:n.offsetX,y:n.offsetY,modifiers:e._getModifiers(n),button:{button:s[n.button],count:2}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("touchstart",(e=>{e.preventDefault();var n=e.target.getBoundingClientRect(),o={window_uid:t,class_name:"MouseEvent",type:"BUTTON_DOWN",x:Math.round(e.targetTouches[0].pageX-n.left),y:Math.round(e.targetTouches[0].pageY-n.top),modifiers:0,button:{button:s[e.button],count:1}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("mouseup",(n=>{n.preventDefault();var o={window_uid:t,class_name:"MouseEvent",type:"BUTTON_UP",x:n.offsetX,y:n.offsetY,modifiers:e._getModifiers(n),button:{button:s[n.button],count:1}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("touchend",(e=>{e.preventDefault();var n=e.target.getBoundingClientRect(),o={window_uid:t,class_name:"MouseEvent",type:"BUTTON_UP",x:Math.round(e.targetTouches[0].pageX-n.left),y:Math.round(e.targetTouches[0].pageY-n.top),modifiers:0,button:{button:s[e.button],count:1}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("mousemove",(n=>{n.preventDefault();var o={window_uid:t,class_name:"MouseEvent",type:0===n.buttons?"MOVE":"DRAG",x:n.offsetX,y:n.offsetY,modifiers:e._getModifiers(n),move:{buttons:n.buttons}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("touchmove",(e=>{e.preventDefault();var n=e.target.getBoundingClientRect(),o={window_uid:t,class_name:"MouseEvent",type:"DRAG",x:Math.round(e.targetTouches[0].pageX-n.left),y:Math.round(e.targetTouches[0].pageY-n.top),modifiers:0,move:{buttons:1}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("mouseleave",(n=>{var o={window_uid:t,class_name:"MouseEvent",type:"BUTTON_UP",x:n.offsetX,y:n.offsetY,modifiers:e._getModifiers(n),button:{button:s[n.button],count:1}};this.sendJsonData(o)}),!1),this.videoElt.addEventListener("wheel",(n=>{n.preventDefault();var o=n.wheelDeltaY?n.wheelDeltaY===-3*n.deltaY:0===n.deltaMode,i=n.deltaX,a=n.deltaY;i=0===i?i:-i/Math.abs(i)*1,a=0===a?a:-a/Math.abs(a)*1;var s={window_uid:t,class_name:"MouseEvent",type:"WHEEL",x:n.offsetX,y:n.offsetY,modifiers:e._getModifiers(n),wheel:{dx:i,dy:a,isTrackpad:o?1:0}};this.sendJsonData(s)}),{passive:!1})}},e.prototype.disconnect=function(){if(this.videoElt&&(this.videoElt.src=""),this.pc){e.remoteCall(this.srvurl+"/api/hangup?peerid="+this.pc.peerid,{},this.commsFetch).then(this._handleHttpErrors).catch((e=>this.onError("hangup "+e)));try{this.pc.close()}catch(e){console.warn("Failure close peer connection:"+e)}this.pc=null,this.dataChannel=null}},e.prototype.onReceiveGetIceServers=function(t,n,o,i,a){this.iceServers=t,this.pcConfig=t||{iceServers:[]};try{this.createPeerConnection();var s=this.srvurl+"/api/call?peerid="+this.pc.peerid+"&url="+encodeURIComponent(n);o&&(s+="&audiourl="+encodeURIComponent(o)),i&&(s+="&options="+encodeURIComponent(i)),a&&this.pc.addStream(a),this.earlyCandidates.length=0;var r=this;this.pc.createOffer(this.mediaConstraints).then((function(t){console.log("Create offer:"+JSON.stringify(t)),r.pc.setLocalDescription(t,(function(){e.remoteCall(s,{method:"POST",body:JSON.stringify(t)},r.commsFetch).then(r._handleHttpErrors).then((e=>e.json())).catch((e=>r.onError("call "+e))).then((e=>r.onReceiveCall.call(r,e))).catch((e=>r.onError("call "+e)))}),(function(e){console.warn("setLocalDescription error:"+JSON.stringify(e))}))}),(function(e){alert("Create offer error:"+JSON.stringify(e))}))}catch(e){this.disconnect(),alert("connect error: "+e)}},e.prototype.getIceCandidate=function(){e.remoteCall(this.srvurl+"/api/getIceCandidate?peerid="+this.pc.peerid,{},this.commsFetch).then(this._handleHttpErrors).then((e=>e.json())).then((e=>this.onReceiveCandidate.call(this,e))).catch((e=>bind.onError("getIceCandidate "+e)))},e.prototype.createPeerConnection=function(){console.log("createPeerConnection  config: "+JSON.stringify(this.pcConfig)+" option:"+JSON.stringify(this.pcOptions)),this.pc=new RTCPeerConnection(this.pcConfig,this.pcOptions);var e=this.pc;e.peerid=Math.random();var t=this;e.onicecandidate=function(e){t.onIceCandidate.call(t,e)},e.onaddstream=function(e){t.onAddStream.call(t,e)},e.oniceconnectionstatechange=function(n){console.log("oniceconnectionstatechange  state: "+e.iceConnectionState),t.videoElt&&("connected"===e.iceConnectionState?t.videoElt.style.opacity="1.0":"disconnected"===e.iceConnectionState?t.videoElt.style.opacity="0.25":"failed"===e.iceConnectionState||"closed"===e.iceConnectionState?t.videoElt.style.opacity="0.5":"new"===e.iceConnectionState&&t.getIceCandidate.call(t))},e.ondatachannel=function(e){console.log("remote datachannel created:"+JSON.stringify(e)),e.channel.onopen=function(){console.log("remote datachannel open"),t.videoElt.dispatchEvent(new CustomEvent("RemoteDataChannelOpen",{detail:e}))},e.channel.onmessage=function(e){console.log("remote datachannel recv:"+JSON.stringify(e.data))}},e.onicegatheringstatechange=function(){"complete"===e.iceGatheringState&&e.getReceivers().forEach((e=>{e.track&&"video"===e.track.kind&&void 0!==e.getParameters&&console.log("codecs:"+JSON.stringify(e.getParameters().codecs))}))};try{this.dataChannel=e.createDataChannel("ClientDataChannel");var n=this.dataChannel;n.onopen=function(){console.log("local datachannel open"),t.videoElt.dispatchEvent(new CustomEvent("LocalDataChannelOpen",{detail:{channel:n}}))},n.onmessage=function(e){console.log("local datachannel recv:"+JSON.stringify(e.data))},n.onclose=function(e){console.log("dataChannel.onclose triggered"),t.onClose()}}catch(e){console.warn("Cannot create datachannel error: "+e)}return console.log("Created RTCPeerConnection with config: "+JSON.stringify(this.pcConfig)+"option:"+JSON.stringify(this.pcOptions)),e},e.prototype.onIceCandidate=function(e){e.candidate&&e.candidate.candidate?this.pc.currentRemoteDescription?this.addIceCandidate(this.pc.peerid,e.candidate):this.earlyCandidates.push(e.candidate):console.log("End of candidates.")},e.prototype.addIceCandidate=function(t,n){e.remoteCall(this.srvurl+"/api/addIceCandidate?peerid="+t,{method:"POST",body:JSON.stringify(n)},this.commsFetch).then(this._handleHttpErrors).then((e=>e.json())).then((e=>{console.log("addIceCandidate ok:"+e)})).catch((e=>this.onError("addIceCandidate "+e)))},e.prototype.onAddStream=function(e){console.log("Remote track added:"+JSON.stringify(e)),this.videoElt.srcObject=e.stream;var t=this.videoElt.play();if(void 0!==t){var n=this;t.catch((function(e){console.warn("error:"+e),n.videoElt.setAttribute("controls",!0)}))}},e.prototype.onReceiveCall=function(e){var t=this;console.log("offer: "+JSON.stringify(e));var n=new RTCSessionDescription(e);this.pc.setRemoteDescription(n,(function(){for(console.log("setRemoteDescription ok");t.earlyCandidates.length;){var e=t.earlyCandidates.shift();t.addIceCandidate.call(t,t.pc.peerid,e)}t.getIceCandidate.call(t)}),(function(e){console.warn("setRemoteDescription error:"+JSON.stringify(e))}))},e.prototype.onReceiveCandidate=function(e){if(console.log("candidate: "+JSON.stringify(e)),e){for(var t=0;t<e.length;t++){var n=new RTCIceCandidate(e[t]);console.log("Adding ICE candidate :"+JSON.stringify(n)),this.pc.addIceCandidate(n,(function(){console.log("addIceCandidate OK")}),(function(e){console.warn("addIceCandidate error:"+JSON.stringify(e))}))}this.pc.addIceCandidate()}},e.prototype.onError=function(e){console.warn("onError:"+e)},e}();void 0!==e.exports?e.exports=t:window.WebRtcStreamer=t},147:e=>{"use strict";e.exports={version:"0.16.0"}}}]);