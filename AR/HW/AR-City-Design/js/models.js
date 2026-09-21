AFRAME.registerComponent("models", {
  init: async function() {
    let data = await fetch("./models.json");
    let models = await data.json()
    Object.keys(models).map((code)=>{
      this.createMarker(models[code]);
    })
  },
  createMarker: function(data) {
    let scene = document.querySelector("a-scene");
    let model = document.createElement("a-gltf-model");
    model.setAttribute("id", `model-${data.name}`);
    model.setAttribute("src", data.url);
    scene.appendChild(model);
  }
});