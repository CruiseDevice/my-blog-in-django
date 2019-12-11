<template>
  <div class="container">
    <div class="card">
      <div class="card-body">
        <div class="card-title">
          <h4>{{postById.title}}</h4>
          <small class="text-muted">{{postById.published_date | date}}</small>
        </div>
        <div v-html="postById.text"></div>
      </div>
    </div>
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
<style>
  .card {
    margin-top: 2em;
  }
</style>
