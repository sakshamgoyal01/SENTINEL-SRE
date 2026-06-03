def correlate_trace(event: dict):

    trace_id = event.get("trace_id")

    if trace_id:

        event["correlated"] = True

    else:

        event["correlated"] = False

    return event