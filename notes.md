# Plotly express narwhalificantion notes

Everything happens in `make_figure`

- `apply_default_cascade` does not affect dataframe ✅
- `build_dataframe` ✅
  - `process_args_into_dataframe` ✅
- `process_dataframe_hierarchy` ✅
  - `_check_dataframe_all_leaves` ✅
- `process_dataframe_pie`
- `process_dataframe_timeline`: ✅
- `infer_config` ✅
  - `make_mapping` does not affect dataframe ✅
  - `make_trace_spec`: does not affect dataframe ✅
- `get_groups_and_orders`: ✅
- `make_trace_kwargs`  ✅

## Tests

- packages/python/plotly/plotly/tests/test_optional/test_px/test_colors.py ✅
packages/python/plotly/plotly/tests/test_optional/test_px/test_facets ✅
packages/python/plotly/plotly/tests/test_optional/test_px/test_imshow ✅
packages/python/plotly/plotly/tests/test_optional/test_px/test_marginals ✅
packages/python/plotly/plotly/tests/test_optional/test_px/test_pandas_backend.py 🚧
packages/python/plotly/plotly/tests/test_optional/test_px/test_px ✅
packages/python/plotly/plotly/tests/test_optional/test_px/test_px_functions.py 🚧
packages/python/plotly/plotly/tests/test_optional/test_px/test_px_hover.py ✅
packages/python/plotly/plotly/tests/test_optional/test_px/test_px_input.py 🚧
packages/python/plotly/plotly/tests/test_optional/test_px/test_px_wide.py 🚧
packages/python/plotly/plotly/tests/test_optional/test_px/test_trendline.py 🚧 (Timeseries only is failing)