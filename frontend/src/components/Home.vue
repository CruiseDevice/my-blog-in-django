<template>
  <div>
    <center>
      <div class="row">
            <div class="card mb-3">
              <img class="card-img-top rounded-circle" src="./../../static/img/10258150.png" alt="cruisedevice">
              <div class="card-body">
                <h3 class="card-title">Akash's Blog</h3>
                <p class="card-text"><small class="text-muted">Developer</small></p>
                <div class="social-links">
                  <a href="https://www.linkedin.com/in/iakashchavan/">Linkedin</a>
                  <a href="https://github.com/CruiseDevice">Github</a>
                  <a href="https://twitter.com/CruiseDevice">Twitter</a>
                </div>
              </div>
            </div>
      </div>
    </center>
    <div v-for="post in getposts" :key="post.id">
      <div class="card mb-3 post-card">
          <div class="card-body">
            <div class="card-title">
              <router-link :to="`/blog/${post.id}`"><h5 class="card-title">{{post.title}}</h5></router-link>
              <small class="text-muted">{{post.published_date | date}}</small>
            </div>
            <p class="card-text">{{truncate(post.text, 300, '...')}}</p>
            <footer class="badge"  v-for="tag in post.tagList" :key="tag.id">
              <span class="badge badge-secondary">{{tag}}</span>
            </footer>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Home',
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

<style scoped>
.row{
  display: flex-shrink;
}

img {
  width: 10rem;
  height: 1 0rem;
}
.card {
  width: 60rem;
  margin: 0 auto;
  float: none;
  margin-bottom: 10px;
  margin-top: 1em;
}
</style>
