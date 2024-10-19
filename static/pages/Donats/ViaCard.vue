<script>
export default {
  name: "ViaCard"
}
</script>

<template>
  <div>
    <form class="grid grid-cols-1 md:grid-cols-2 gap-10">
      <div>
        <label class="title" for="name">номер карты:</label>
        <input type="text" id="name" class="w-full border border-gray-300 rounded p-2 bg-white" value="4400 4440 4444 4444" readonly>
      </div>
    
      <div>
        <label class="title" for="dob">cvv:</label>
        <input type="text" id="dob" class="w-full border border-gray-300 rounded p-2 bg-white" value="777" readonly>
      </div>
    
      <div>
        <label class="title" for="iin">ИМЯ на карте:</label>
        <input type="text" id="iin" class="w-full border border-gray-300 rounded p-2 bg-white" value="MAKSADBEK" readonly>
      </div>
    
      <div class="relative">
        <label class="title" for="phone">Сумма:</label>
        <input type="text" id="phone" class="w-full border border-gray-300 rounded p-2 bg-white" value="1000" readonly>
        <p class="absolute right-3 top-1/2">т</p>
      </div>
    </form>
    <div class="flex my-10">
<!--      <label class="custom-checkbox">-->
<!--        <input type="checkbox">-->
<!--        <span class="checkmark"></span>-->
<!--      </label>-->
      <input type="checkbox">
      <p class="font-medium text-base uppercase ml-6" style="letter-spacing: 2px">Я подтверждаю, что ознакомлен с правилами внесения пожертвований.</p>
    </div>
    <div class="w-full overflow-hidden" style="border-radius: 8px">
      <button class="uppercase px-6 py-4 text-center w-full text-white font-medium" style="background-color: #0072AB">Отправить донат</button>
    </div>
  </div>
</template>

<style scoped>
.title{
  font-weight: 500;
  @apply text-base uppercase;
  letter-spacing:3px;
  line-height: 23px;
}
.custom-checkbox {
  display: inline-block;
  position: relative;
  padding-left: 35px;
  cursor: pointer;
  font-size: 22px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.custom-checkbox input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 24px;
  width: 24px;
  background-color: #f9f9f9;
  border: 2px solid #eaeaea;
  border-radius: 10px; /* Закругленные углы */
  transition: all 0.3s;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.05); /* Лёгкая тень */
}

.custom-checkbox input:checked ~ .checkmark {
  background-color: #2196F3;
  border: 2px solid #2196F3;
}

.custom-checkbox .checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.custom-checkbox input:checked ~ .checkmark:after {
  display: block;
}

.custom-checkbox .checkmark:after {
  left: 8px;
  top: 5px;
  width: 8px;
  height: 13px;
  border: solid white;
  border-width: 0 3px 3px 0;
  transform: rotate(45deg);
}

</style>