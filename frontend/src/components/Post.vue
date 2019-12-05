<template>
  <div>
    {{postById}}
  </div>
</template>
<script>
export default {
  name: 'Post',
  props: ['post_id'],
  computed: {
    postById () {
      return this.$store.getters.postById(Number(this.post_id))
    }
  }
}
</script>
