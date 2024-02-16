SELECT
    sub.year,
    sub.month,
    sub.customer_id,
    sub.total_monthly_order_value
FROM
    (
        SELECT
            strftime('%Y', o.ordered_at) AS year,
            strftime('%m', o.ordered_at) AS MONTH,
            o.customer_id,
            SUM(oli.unit_price * oli.quantity) AS total_monthly_order_value
        FROM
            orders o
            JOIN order_line_items oli ON o.order_id = oli.order_id
        GROUP BY
            year,
            MONTH,
            o.customer_id
    ) AS sub
    JOIN (
        SELECT
            year,
            MONTH,
            MAX(total_monthly_order_value) AS max_value
        FROM
            (
                SELECT
                    strftime('%Y', o.ordered_at) AS year,
                    strftime('%m', o.ordered_at) AS MONTH,
                    o.customer_id,
                    SUM(oli.unit_price * oli.quantity) AS total_monthly_order_value
                FROM
                    orders o
                    JOIN order_line_items oli ON o.order_id = oli.order_id
                GROUP BY
                    year,
                    MONTH,
                    o.customer_id
            )
        GROUP BY
            year,
            MONTH
    ) AS max_values ON sub.year = max_values.year
    AND sub.month = max_values.month
    AND sub.total_monthly_order_value = max_values.max_value
    JOIN (
        SELECT
            year,
            MONTH,
            MIN(customer_id) AS min_customer_id
        FROM
            (
                SELECT
                    strftime('%Y', o.ordered_at) AS year,
                    strftime('%m', o.ordered_at) AS MONTH,
                    o.customer_id,
                    SUM(oli.unit_price * oli.quantity) AS total_monthly_order_value
                FROM
                    orders o
                    JOIN order_line_items oli ON o.order_id = oli.order_id
                GROUP BY
                    year,
                    MONTH,
                    o.customer_id
            )
        GROUP BY
            year,
            MONTH,
            total_monthly_order_value
    ) AS min_ids ON sub.year = min_ids.year
    AND sub.month = min_ids.month
    AND sub.customer_id = min_ids.min_customer_id
ORDER BY
    sub.year ASC,
    sub.month ASC;