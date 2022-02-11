<template>
  <aside
    class="my-3 overflow-auto border-0 sidenav navbar navbar-vertical navbar-expand-xs border-radius-xl"
    :class="this.$store.state.isRTL ? 'me-3 rotate-caret' : 'ms-3'"
    id="sidenav-main"
  >
    <div class="sidenav-header">
      <i
        class="top-0 p-3 cursor-pointer fas fa-times text-secondary opacity-5 position-absolute end-0 d-none d-xl-none"
        aria-hidden="true"
        id="iconSidenav"
      ></i>
      <a class="m-0 navbar-brand" href="/">
        <img :src="logo" class="navbar-brand-img h-100" alt="main_logo" />
        <span class="ms-1 font-weight-bold">Harry's Website</span>
      </a>
    </div>
    <hr class="mt-0 horizontal dark" />
  </aside>
</template>
<script>
import logo from "@/assets/img/avatar.png";

export default {
  name: "index",
  components: {
  },
  data() {
    return {
      logo,
    };
  },
  props: ["custom_class"],
};
</script>
