<script lang="ts" setup>
import SearchInput from "~/components/SearchInput.vue";
import MappingItemList from "~/components/MappingItemList.vue";
import type { PaginationResult } from "~/utils/types/APIInterfaces";

const localPath = useLocalePath();
const route = useRoute();
const router = useRouter();
const searchText = ref<string>("");
const result = ref<PaginationResult | null>(null);
const loading = ref<boolean>(false);
const didBackendCallOnce = ref<boolean>(false);
const page = ref<number>(1); // init page number always with one
const itemsPerPage = 20; // define the max numbers of items per page

const navigate = async () => {
  await router.push({
    path: localPath("/search"),
    query: {
      searchText: searchText.value,
      page: 1,
    },
  });
};

const doSearch = async () => {
  if (String(searchText.value) !== "") {
    didBackendCallOnce.value = true; // is never set to false if a backend call was made at least once
    loading.value = true;
    try {
      const offset = (page.value - 1) * itemsPerPage;
      const { refresh, data, pending } = await search(
        searchText.value,
        undefined,
        itemsPerPage,
        offset
      );
      if (pending.value && data.value === null) {
        await refresh();
      }
      result.value = data.value;
    } finally {
      loading.value = false;
    }
  }
};

watch(
  () => route.query.searchText,
  async (term) => {
    searchText.value = term as string;
    await doSearch();
  }
);

// watch route query-param "page" on changes
watch(
  () => route.query.page,
  async (newPage) => {
    page.value = parseInt(newPage + "");
    await doSearch();
  }
);

onMounted(async () => {
  const parsedPageQueryParam = parseInt(route.query.page + "");
  page.value = parsedPageQueryParam || 1;
  searchText.value = (route.query.searchText as string) || "";
  await doSearch();
});
</script>

<template>
  <NuxtLayout name="main">
    <IPButton @click.prevent="router.push({ path: localPath('/') })">
      {{ $t("back_to_category_list") }}
    </IPButton>
    <hr class="my-4" />
    <SearchInput v-model="searchText" @click="navigate" />
    <div v-if="!didBackendCallOnce && !loading">
      {{ $t("search_typing_hint") }}
    </div>
    <div v-else-if="loading">
      {{ $t("loading") }}
    </div>
    <div v-else-if="result && result.totalCount === 0">
      {{ $t("no_result") }}
    </div>
    <div v-else-if="result && result.totalCount > 0" class="my-4">
      <PaginationContainer
        :total-count="result.totalCount"
        :current-page="page"
        :items-per-page="itemsPerPage"
        :route="{ query: { searchText } }"
      />
      <MappingItemList :category-list="result.data" />
      <PaginationContainer
        :total-count="result.totalCount"
        :current-page="page"
        :items-per-page="itemsPerPage"
        :route="{ query: { searchText } }"
      />
    </div>
  </NuxtLayout>
</template>
