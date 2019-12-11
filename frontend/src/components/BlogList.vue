<template>
    <div>
        <div v-for="post in getposts" :key="post.id">
          <div class="card mb-3 post-card">
              <div class="card-body">
                <router-link :to="`/blog/${post.id}`"><h5 class="card-title">{{post.title}}</h5></router-link>
                <small class="text-muted">{{post.published_date | date}}</small>
                <p class="card-text">{{truncate(post.text, 300, '...')}}</p>
              </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'BookList',
  created () {
    this.$store.dispatch('fetchblogs')
  },
  computed: {
    ...mapGetters([
      'getposts'
    ])
  },
  methods: {
    truncate (text, length, clamp) {
      clamp = clamp || '...'
      var node = document.createElement('div')
      node.innerHTML = text
      var content = node.textContent
      return content.length > length ? content.slice(0, length) + clamp : content
    }
  }
}
</script>
<style>
  .card {
  width: 60rem;
  margin: 0 auto;
  float: none;
  margin-bottom: 10px;
  margin-top: 1em;
}
</style>
