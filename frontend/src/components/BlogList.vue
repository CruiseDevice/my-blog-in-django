
<template>
    <div>
        <div v-for="post in getposts" :key="post.id">
          <div class="card mb-3 post-card">
              <div class="card-body">
                <a href=""><h5><p class="card-title">{{post.title}}</p></h5></a>
                <p class="card-text">{{truncate(post.text, 300, '...')}}</p>
              </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
  name: 'BookList',
  created () {
    this.$store.dispatch('fetchblogs')
  }
}
</script>
