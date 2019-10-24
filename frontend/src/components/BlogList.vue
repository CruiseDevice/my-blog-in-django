<template>
    <div>

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
