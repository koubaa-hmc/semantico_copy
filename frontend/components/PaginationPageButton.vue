<script lang="ts" setup>
import type { RouteLocation, RouteLocationRaw } from "vue-router";
import type { NuxtLink } from "#build/components.d.ts";

const props = defineProps({
  disabled: {
    type: Boolean,
    required: false,
    default: false,
  },
  secondary: {
    type: Boolean,
    required: false,
    default: false,
  },
  route: {
    type: Object as PropType<Partial<RouteLocation>>,
    required: false,
    default: () => {
      return {};
    },
  },
});

/** Calculates the style of the element */
const classes = computed(() => {
  const generalClasses =
    "h-11 px-2 border border-hmc-blue-dark rounded-lg text-hmc-blue-dark flex items-center justify-center select-none ";
  if (props.disabled === true) {
    return generalClasses + "pointer-events-none bg-hmc-grey font-bold";
  } else if (props.secondary === true) {
    return (
      generalClasses +
      "text-hmc-blue hover:bg-hmc-green hover:text-white hover:cursor-pointer"
    );
  } else {
    return (
      generalClasses +
      "hover:bg-hmc-blue-light hover:text-white hover:cursor-pointer"
    );
  }
});

/** References the NuxtLink element used in the click handler */
const linkRef = ref<typeof NuxtLink>();

/**
 * Ensure that clicking on the parent element of NuxtLink also triggers a page change,
 * this is required if the user does not correctly hit the <a> element
 */
const clickHandler = () => {
  if (linkRef.value) {
    linkRef.value.$el.click();
  }
};
</script>

<template>
  <div :class="classes" @click.stop="clickHandler">
    <NuxtLink ref="linkRef" :to="(route as RouteLocationRaw)" @click.stop>
      <slot />
    </NuxtLink>
  </div>
</template>
