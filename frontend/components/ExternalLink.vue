<script lang="ts" setup>
defineProps({
  secondary: {
    type: Boolean,
    required: false,
    default: false,
  },
});
</script>

<template>
  <a
    :class="[secondary ? 'text-white' : 'text-hmc-blue']"
    class="hover:text-hmc-blue-light cursor-pointer"
    rel="noreferrer"
    target="_blank"
  >
    <slot />
  </a>
</template>
