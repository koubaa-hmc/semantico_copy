<script lang="ts" setup>
const props = defineProps({
  secondary: {
    type: Boolean,
    required: false,
    default: false,
  },
  disabled: {
    type: Boolean,
    required: false,
    default: false,
  },
});

const classes = computed(() => {
  // default link
  let c = "text-hmc-blue hover:text-hmc-blue-light cursor-pointer";
  // link is secondary link
  if (props.secondary && !props.disabled) {
    c = "text-white hover:text-hmc-blue-light cursor-pointer";
  }
  // link is disabled
  if (props.disabled) {
    c = "text-gray-400 cursor-default pointer-none";
  }

  return c;
});
</script>

<template>
  <NuxtLink :class="classes">
    <slot />
  </NuxtLink>
</template>
