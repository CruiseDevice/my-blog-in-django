<template>
  <div id="app">
    <NavMenu />
    <router-view/>
  </div>
</template>

<script>
// import NavMenu from '../src/components/NavMenu.vue'
import NavMenu from '../src/components/NavMenu'

export default {
  name: 'App',
  components: {
    NavMenu
  }
}
</script>
<style>
    #app {
        overflow-x: hidden;
    }
</style>
