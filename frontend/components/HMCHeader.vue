<script lang="ts" setup>
import type { LocaleObject } from "@nuxtjs/i18n/dist/runtime/composables";
import InternalLink from "~/components/InternalLink.vue";
import IPButton from "~/components/IPButton.vue";
import ExternalLink from "~/components/ExternalLink.vue";
import SearchInputButton from "~/components/SearchInputButton.vue";

const scrollingThreshold = 20;
const scrollPosition = ref<number>(0);
const checkLoggedIn = false;

const { setLocale, locales } = useI18n();
const localePath = useLocalePath();

const isScrolled = computed(() => scrollPosition.value > scrollingThreshold);

const updateScrollPosition = (event: WindowEventMap["scroll"]) => {
  scrollPosition.value = (event.currentTarget as Window).scrollY;
};

onMounted(() => {
  if (process.client) {
    window.addEventListener("scroll", updateScrollPosition);
  }
});
onUnmounted(() => {
  if (process.client) {
    window.removeEventListener("scroll", updateScrollPosition);
  }
});

const availableLocales = computed(() => {
  return locales.value;
});
</script>

<template>
  <header
    :class="{ 'lg:h-20 header-shadow': isScrolled }"
    class="sticky top-0 bg-white lg:mb-0 mb-4 py-2 h-16 lg:h-24"
  >
    <div class="container mx-auto h-full">
      <div class="flex flex-wrap justify-between items-center h-full my-auto">
        <InternalLink :to="localePath('/')">
          <img
            src="~/assets/images/HMC_Logo.svg"
            alt="HMC Logo"
            width="400"
            height="53"
          />
        </InternalLink>
        <div class="flex flex-col h-full invisible md:visible">
          <div
            class="flex flex-wrap justify-end space-x-2"
            :class="{ hidden: isScrolled }"
          >
            <InternalLink
              v-for="loc in (availableLocales as LocaleObject[])"
              :key="loc.code"
              :disabled="$i18n.locale === loc.code"
              class="uppercase"
              @click.prevent.stop="setLocale(loc.code)"
            >
              {{ loc.code }}
            </InternalLink>
          </div>
          <div
            class="space-x-10 flex flex-wrap justify-end items-center my-auto"
          >
            <IPButton v-if="checkLoggedIn">
              {{ $t("btn_txt_sync_to_gitlab") }}
            </IPButton>
            <ExternalLink v-if="checkLoggedIn" class="uppercase">
              {{ $t("btn_txt_logout") }}
            </ExternalLink>
            <SearchInputButton />
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style>
.header-shadow {
  box-shadow: 0 0 10px 0 rgba(117, 117, 117, 0.5);
}
</style>
