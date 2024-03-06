<script lang="ts" setup>
import SearchInput from "~/components/SearchInput.vue";
import ExternalLink from "~/components/ExternalLink.vue";

const route = useRoute();
const router = useRouter();
const localPath = useLocalePath();
const showInput = ref<boolean>(false);
const searchText = ref<string>((route.query.searchText as string) || "");
const searchInput = ref<typeof SearchInput | null>(null);
const searchInputContainer = ref<HTMLDivElement | null>(null);

watch(
  () => route.query.searchText,
  (term) => {
    searchText.value = term as string;
  }
);

onMounted(() => {
  if (process.client) {
    document.addEventListener("click", boundingBoxClickHandler);
  }
});
onUnmounted(() => {
  if (process.client) {
    document.removeEventListener("click", boundingBoxClickHandler);
  }
});

const boundingBoxClickHandler = (e: MouseEvent) => {
  if (showInput.value && isClickOutSideOfContainer(e.clientX, e.clientY)) {
    toggleInput();
  }
};

const isClickOutSideOfContainer = (cX: number, cY: number) => {
  const bbox = searchInputContainer.value!.getBoundingClientRect();
  return !(
    cX >= bbox.x && // check left
    cX <= bbox.x + bbox.width && // check right
    cY >= bbox.y && // check top
    cY <= bbox.y + bbox.height
  );
};

const toggleInput = () => {
  showInput.value = !showInput.value;
  nextTick(() => searchInput.value!.focus());
};

const doSearch = () => {
  router.push({
    path: localPath("/search"),
    query: {
      searchText: searchText.value,
    },
  });
};
</script>

<template>
  <div :class="{ 'h-10 py-2': !showInput }">
    <ExternalLink
      class="uppercase"
      :class="{ hidden: showInput }"
      @click.prevent="toggleInput"
    >
      {{ $t("btn_txt_search") }}
    </ExternalLink>
    <div ref="searchInputContainer">
      <SearchInput
        ref="searchInput"
        v-model="searchText"
        small
        :class="{ hidden: !showInput }"
        @click="doSearch"
      />
    </div>
  </div>
</template>
