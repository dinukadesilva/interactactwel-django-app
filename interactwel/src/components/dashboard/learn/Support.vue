<template>
  <b-row>
    <b-col cols="8">
      <b-card-body title="Support">
        <b-card-text>
          Please contact Dr. Meghna Babbar-Sebens (meghna@oregonstate.edu) if you have questions about InterACTWEL.
        </b-card-text>
      </b-card-body>
    </b-col>
  </b-row>
</template>

<script>
import Header from './../../Header.vue';
import Footer from './../../Footer.vue';

export default {
  name: 'Docs',
  components: {
    Header, Footer,
  },

  data() {
    return {
    };
  },

  mounted() {
  }
  ,

  methods: {},

};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .map-wrapper {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        min-height: calc(60vh);
    }

    .widget {
        background-color: #f7f7f7;
        padding: 1rem;
        border: 1px solid #efefef;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .widget-title {
        font-size: 16px;
        font-weight: 700;
    }
</style>
