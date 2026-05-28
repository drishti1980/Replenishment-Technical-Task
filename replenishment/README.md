### Replenishment

Replenishment Suggestion Tools

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app replenishment
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/replenishment
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit



This module defines Replenishment logics like Stock On hand calculations

You will find below as a calculation rules which says how much stock is there and what needs to be ordered 

This method needs to run server side.. execution based on button click and it should provide suggestions to calculate for child table
# For each stock-enabled, non-disabled Item in the warehouse:
 
current_stock      = on-hand qty in the selected warehouse
issued_qty         = total qty issued from this warehouse
                     over the last `lookback_days`
avg_daily_usage    = issued_qty / lookback_days
lead_time_days     = Item.lead_time_days  (fallback to 7 if blank)
safety_stock_qty   = avg_daily_usage * safety_stock_days
reorder_point      = (avg_daily_usage * lead_time_days) + safety_stock_qty
open_po_qty        = sum of qty on submitted Purchase Orders for this
                     item + warehouse where status is not Closed/Completed
                     and qty not yet received
 
if current_stock + open_po_qty < reorder_point:
    target_qty    = reorder_point + (avg_daily_usage * lead_time_days)
    suggested_qty = target_qty - current_stock - open_po_qty
    # round UP to Item.min_order_qty if set, else to nearest whole unit
    add row to child table
else:
    skip
