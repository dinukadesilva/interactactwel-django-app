<template>
  <div
    id="graph"
    class="card"
  >
  <div class="card-header">
      <div class="row">
        <div class="col-8">
          <strong>Sub-basins</strong>
        </div>
        <div class="col-4">
          <div class="form-group">
            <v-select
              :options="options"
              v-model="selectedSubBasin"
            >
            </v-select>
          </div>
        </div>
      </div>
    </div>
    <div class="card-body no-padding">
      <b-tabs card>
        <b-tab title="Stream Flow">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>
                  <flowout-stream-sub-graph :selected-basin-id="selectedSubBasin.code" v-bind:base-graph="false"></flowout-stream-sub-graph>
                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <flowout-stream-sub-graph :selected-basin-id="selectedSubBasin.code" v-bind:base-graph="true"></flowout-stream-sub-graph>
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Sediment transported with water out of reach during time step">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Nitrate transported with water out of reach during time step">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Amount of dissolved oxygen transported with water out of reach during time step">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Stream temperature in reach">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Total nitrogen in surface runoff">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Total phosphorus in surface runoff">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <img
                      class="img-fluid"
                      src="../../../../assets/graph-placeholder.png"
                  >
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>
<script>

import GwqGraph from "@/components/dashboard/projects/charts/data/gwqGraph";
import WaterYieldGraph from "@/components/dashboard/projects/charts/data/waterYieldGraph";
import SedimentYieldGraph from "@/components/dashboard/projects/charts/data/sedimentYieldGraph";
import EtGraph from "@/components/dashboard/projects/charts/data/etGraph";
import SwGraph from "@/components/dashboard/projects/charts/data/swGraph";
import FlowoutStreamSubGraph from "@/components/dashboard/projects/charts/data/flowoutStreamSubGraph";
export default {
  name: 'Actions',
  components: {FlowoutStreamSubGraph, SwGraph, EtGraph, SedimentYieldGraph, WaterYieldGraph, GwqGraph},
  props: {},
  data() {
    return {};
  },
  watch: {},
  mounted() {

  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
