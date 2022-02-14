<template>
  <div class="card mb-4">
    <div class="card-header pb-0">
      <h6>Web Table</h6>
    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th
                class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              >
                Web
              </th>
              <th
                class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2"
              >
                Function
              </th>
              <th
                class="text-left text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              >
                Address
              </th>
              <th
                class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              >
                Status
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="ip in ipaddr" v-bind:key="ip">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <vsud-avatar
                      :img="img1"
                      size="sm"
                      border-radius="lg"
                      class="me-3"
                      alt="user1"
                      :href="'http://' + ip + ':8096'"
                    />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm" :href="'http://' + ip + ':8096'">Jellyfin</h6>
                    <p class="text-xs text-secondary mb-0">
                      {{ ip }}
                    </p>
                  </div>
                </div>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">Media</p>
                <p class="text-xs text-secondary mb-0">
                  Anime, Movies, TV Shows
                </p>
              </td>
              <td class="align-middle text-left">
                <a :href="'http://' + ip + ':8096'"> {{ ip }}:8096 </a>
              </td>
              <td class="align-middle text-center text-sm">
                <vsud-badge color="success" variant="gradient" size="sm"
                  >ONLINE</vsud-badge
                >
              </td>
            </tr>
            <tr>
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <vsud-avatar
                      :img="img2"
                      class="me-3"
                      size="sm"
                      border-radius="lg"
                      alt="user2"
                      href="https://vault.bitwarden.com/"
                    />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm" href="https://vault.bitwarden.com/">Bitwarden</h6>
                    <p class="text-xs text-secondary mb-0">bitwarden.com</p>
                  </div>
                </div>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">Password Manager</p>
                <p class="text-xs text-secondary mb-0">
                  Store password across devices
                </p>
              </td>
              <td class="align-middle text-left">
                <a href="https://vault.bitwarden.com/"> vault.bitwarden.com </a>
              </td>
              <td class="align-middle text-center text-sm">
                <vsud-badge color="success" variant="gradient" size="sm"
                  >ONLINE</vsud-badge
                >
              </td>
            </tr>
            <tr>
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <vsud-avatar
                      :img="img3"
                      class="me-3"
                      size="sm"
                      border-radius="lg"
                      alt="user2"
                      href="https://app.raindrop.io/"
                    />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm" src="https://app.raindrop.io/">Raindrop</h6>
                    <p class="text-xs text-secondary mb-0">raindrop.io</p>
                  </div>
                </div>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">Bookmark Manager</p>
                <p class="text-xs text-secondary mb-0">
                  Store bookmark across browsers
                </p>
              </td>
              <td class="align-middle text-left">
                <a href="https://app.raindrop.io/"> app.raindrop.io </a>
              </td>
              <td class="align-middle text-center text-sm">
                <vsud-badge color="success" variant="gradient" size="sm"
                  >ONLINE</vsud-badge
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import VsudAvatar from "@/components/VsudAvatar.vue";
import VsudBadge from "@/components/VsudBadge.vue";
import img1 from "../../assets/img/team-2.png";
import img2 from "../../assets/img/team-3.png";
import img3 from "../../assets/img/team-4.png";
import img4 from "../../assets/img/team-3.jpg";
import img5 from "../../assets/img/team-2.jpg";
import img6 from "../../assets/img/team-4.jpg";
import ipjson from "../../ip.json";
import statusjson from "../../status.json";

export default {
  name: "authors-table",
  data() {
    return {
      img1,
      img2,
      img3,
      img4,
      img5,
      img6,
      ipaddr: ipjson,
      status: statusjson,
    };
  },
  components: {
    VsudAvatar,
    VsudBadge,
  },
};
</script>
