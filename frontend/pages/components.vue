<script lang="ts" setup>
import type { LocaleObject } from "@nuxtjs/i18n/dist/runtime/composables";
import { useI18n, computed } from "#imports";
import ExternalLink from "~/components/ExternalLink.vue";
import InternalLink from "~/components/InternalLink.vue";
import BorderBox from "~/components/BorderBox.vue";
import IPButton from "~/components/IPButton.vue";

const { locale, locales } = useI18n();
const availableLocales = computed(() => {
  return locales.value;
});
const localePath = useLocalePath();
</script>

<template>
  <NuxtLayout name="main">
    <BorderBox>
      <h3>Links</h3>
      <div class="flex flex-wrap justify-between p-4 bg-gray-300">
        <ExternalLink href="https://example.org">
          External Link
        </ExternalLink>
        <ExternalLink secondary href="https://example.org">
          External Link Secondary
        </ExternalLink>
      </div>
      <div class="flex flex-wrap justify-between p-4 bg-gray-300">
        <InternalLink to="/">
          Internal Link
        </InternalLink>
        <InternalLink secondary to="/">
          Internal Link Secondary
        </InternalLink>
        <InternalLink disabled to="/">
          Internal Link Disabled
        </InternalLink>
      </div>
    </BorderBox>
    <BorderBox>
      <h3>Buttons</h3>
      <div class="flex flex-wrap justify-between p-4 bg-gray-300">
        <IPButton> Button Primary </IPButton>
        <IPButton secondary>
          Button Secondary
        </IPButton><IPButton disabled>
          Button Disabled
        </IPButton>
      </div>
    </BorderBox>
    <BorderBox>
      <h3>Translation</h3>
      <div class="p-4 bg-gray-300">
        {{ $t("instant_language_switcher") }}
        <form>
          <select v-model="locale">
            <option
              v-for="loc in (availableLocales as LocaleObject[])"
              :key="loc.code"
              :value="loc.code"
            >
              {{ loc.name }}
            </option>
          </select>
        </form>
        <br />
        <br />
        {{ $t("language_link_examples") }}
        <br />
        <NuxtLink :to="localePath('index')">
          {{ $t("home_via_name") }}
        </NuxtLink>
        <br />
        <NuxtLink :to="localePath('/')">
          {{ $t("home_via_path") }}
        </NuxtLink>
        <br />
        <NuxtLink :to="localePath('/', 'en')">
          {{ $t("home_lang_en_link") }}
        </NuxtLink>
        <br />
        <NuxtLink :to="localePath('/', 'de')">
          {{ $t("home_lang_de_link") }}
        </NuxtLink>
      </div>
    </BorderBox>
  </NuxtLayout>
</template>
