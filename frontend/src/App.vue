<template>
  <div id="app">
    <NavMenu />
    <router-view/>
  </div>
</template>

<script>
import NavMenu from '../src/components/NavMenu.vue'
export default {
  name: 'App',
  components: {
    NavMenu
  }
}
</script>

<style scoped>
div{
  overflow-x: hidden
}
</style>
