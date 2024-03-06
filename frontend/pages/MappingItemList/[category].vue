<script lang="ts" setup>
import { getCategory } from "~/composables/api";
import {
  isMappingCategoryKey,
  MappingCategory
} from "~/utils/types/MappingCategory";
import type { PaginationResult } from "~/utils/types/APIInterfaces";
import BorderBox from "~/components/BorderBox.vue";
import MappingItemList from "~/components/MappingItemList.vue";
import PaginationContainer from "~/components/PaginationContainer.vue";

const route = useRoute();
const router = useRouter();
const localePath = useLocalePath();
const category = route.params.category.toString();

const itemsPerPage = 16; // define the max numbers of items per page
const page = ref<number>(1); // init page number always with one
const result = ref<PaginationResult | null>(null); // here the fetch result are kept

const fetchData = async (categoryAsString: string) => {
  if (isMappingCategoryKey(categoryAsString)) {
    const offset = (page.value - 1) * itemsPerPage;
    const { refresh, data, pending } = await getCategory(
      MappingCategory[categoryAsString],
      itemsPerPage,
      offset
    );
    if (pending.value && data.value === null) {
      await refresh();
    }
    result.value = data.value;
  }
};

// watch route query-param "page" on changes
watch(
  () => route.query.page,
  async (newPage) => {
    page.value = parseInt(newPage + "");
    await fetchData(category);
  }
);

onMounted(async () => {
  const parsedPageQueryParam = parseInt(route.query.page + "");
  page.value = parsedPageQueryParam || 1;
  await fetchData(category);
});
</script>

<template>
  <NuxtLayout name="main">
    <IPButton @click.prevent="router.push(localePath('/'))">
      {{ $t("back_to_category_list") }}
    </IPButton>
    <hr class="my-4" />
    <div v-if="result && result.totalCount > 0" class="mb-4">
      <PaginationContainer
        :total-count="result.totalCount"
        :items-per-page="itemsPerPage"
        :current-page="page"
      />
      <MappingItemList :category-list="result.data" />
      <PaginationContainer
        :total-count="result.totalCount"
        :items-per-page="itemsPerPage"
        :current-page="page"
      />
    </div>
    <BorderBox v-else>
      {{ $t("no_category_content") }}
    </BorderBox>
  </NuxtLayout>
</template>
