import {generateRequest,retrieveData} from "../utils.js";

document.getElementById("create").addEventListener("click", createRecipe)
async function createRecipe(ev){
  ev.preventDefault()
  const {img , steps , ingredients , name } =  retrieveData(document.querySelector("form"));
  // \r\n joins elements in array in ingredients and steps fields
  try {
    const record = JSON.parse(sessionStorage.getItem("userData"))
    if(record !== null){
      await generateRequest("http://localhost:3030/data/recipes", "post", {
        img , steps : steps.split("\r\n"), ingredients : ingredients.split("\r\n"), name
      }, record.accessToken)
      document.location.href = "index.html"
    }else{
      throw new Error("Not able to create record , login first")
    }
  }catch (er){
    alert(er.message)
  }
}
document.getElementById("logoutBtn").addEventListener("click" , logout)