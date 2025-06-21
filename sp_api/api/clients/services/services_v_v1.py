"""
Generated API client from Swagger/OpenAPI specification.
This file was auto-generated. Do not edit manually.
"""

import json
from typing import (Any, Dict, Generic, List, Optional, TypeVar, Union, cast,
                    overload)

import httpx
from pydantic import BaseModel
# Import all models
from sp_api.api.models.services.services_v1 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class Services_V_v1(Client):
    """
    Selling Partner API for Services - v1

    With the Services API, you can build applications that help service providers get and modify their service orders and manage their resources.
    """

    @overload
    def get_service_job_by_service_job_id(
        self, request: GetServiceJobByServiceJobIdRequest, *args, **kwargs
    ) -> ApiResponse[GetServiceJobByServiceJobIdResponse]:
        """
        Gets details of service job indicated by the provided `serviceJobID`.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           20 |      40 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/serviceJobs/{serviceJobId}", method="GET")
    def get_service_job_by_service_job_id(
        self, *args, **kwargs
    ) -> ApiResponse[GetServiceJobByServiceJobIdResponse]:
        """
        Gets details of service job indicated by the provided `serviceJobID`.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           20 |      40 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetServiceJobByServiceJobIdRequest):
            request = GetServiceJobByServiceJobIdRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetServiceJobByServiceJobIdResponse,
        )

    @overload
    def cancel_service_job_by_service_job_id(
        self, request: CancelServiceJobByServiceJobIdRequest, *args, **kwargs
    ) -> ApiResponse[CancelServiceJobByServiceJobIdResponse]:
        """
        Cancels the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/serviceJobs/{serviceJobId}/cancellations", method="PUT")
    def cancel_service_job_by_service_job_id(
        self, *args, **kwargs
    ) -> ApiResponse[CancelServiceJobByServiceJobIdResponse]:
        """
        Cancels the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CancelServiceJobByServiceJobIdRequest):
            request = CancelServiceJobByServiceJobIdRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CancelServiceJobByServiceJobIdResponse,
        )

    @overload
    def complete_service_job_by_service_job_id(
        self, request: CompleteServiceJobByServiceJobIdRequest, *args, **kwargs
    ) -> ApiResponse[CompleteServiceJobByServiceJobIdResponse]:
        """
        Completes the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/serviceJobs/{serviceJobId}/completions", method="PUT")
    def complete_service_job_by_service_job_id(
        self, *args, **kwargs
    ) -> ApiResponse[CompleteServiceJobByServiceJobIdResponse]:
        """
        Completes the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CompleteServiceJobByServiceJobIdRequest):
            request = CompleteServiceJobByServiceJobIdRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CompleteServiceJobByServiceJobIdResponse,
        )

    @overload
    def get_service_jobs(
        self, request: GetServiceJobsRequest, *args, **kwargs
    ) -> ApiResponse[GetServiceJobsResponse]:
        """
        Gets service job details for the specified filter query.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      40 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/serviceJobs", method="GET")
    def get_service_jobs(self, *args, **kwargs) -> ApiResponse[GetServiceJobsResponse]:
        """
        Gets service job details for the specified filter query.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      40 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetServiceJobsRequest):
            request = GetServiceJobsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetServiceJobsResponse
        )

    @overload
    def add_appointment_for_service_job_by_service_job_id(
        self, request: AddAppointmentForServiceJobByServiceJobIdRequest, *args, **kwargs
    ) -> ApiResponse[SetAppointmentResponse]:
        """
        Adds an appointment to the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/serviceJobs/{serviceJobId}/appointments", method="POST")
    def add_appointment_for_service_job_by_service_job_id(
        self, *args, **kwargs
    ) -> ApiResponse[SetAppointmentResponse]:
        """
        Adds an appointment to the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, AddAppointmentForServiceJobByServiceJobIdRequest):
            request = AddAppointmentForServiceJobByServiceJobIdRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=SetAppointmentResponse
        )

    @overload
    def reschedule_appointment_for_service_job_by_service_job_id(
        self,
        request: RescheduleAppointmentForServiceJobByServiceJobIdRequest,
        *args,
        **kwargs,
    ) -> ApiResponse[SetAppointmentResponse]:
        """
        Reschedules an appointment for the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}",
        method="POST",
    )
    def reschedule_appointment_for_service_job_by_service_job_id(
        self, *args, **kwargs
    ) -> ApiResponse[SetAppointmentResponse]:
        """
        Reschedules an appointment for the service job indicated by the service job identifier specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(
            request, RescheduleAppointmentForServiceJobByServiceJobIdRequest
        ):
            request = RescheduleAppointmentForServiceJobByServiceJobIdRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=SetAppointmentResponse
        )

    @overload
    def assign_appointment_resources(
        self, request: AssignAppointmentResourcesRequest, *args, **kwargs
    ) -> ApiResponse[AssignAppointmentResourcesResponse]:
        """
        Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       2 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/resources",
        method="PUT",
    )
    def assign_appointment_resources(
        self, *args, **kwargs
    ) -> ApiResponse[AssignAppointmentResourcesResponse]:
        """
        Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       2 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, AssignAppointmentResourcesRequest):
            request = AssignAppointmentResourcesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=AssignAppointmentResourcesResponse,
        )

    @overload
    def set_appointment_fulfillment_data(
        self, request: SetAppointmentFulfillmentDataRequest, *args, **kwargs
    ) -> ApiResponse[ErrorList]:
        """
        Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/fulfillment",
        method="PUT",
    )
    def set_appointment_fulfillment_data(
        self, *args, **kwargs
    ) -> ApiResponse[ErrorList]:
        """
        Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SetAppointmentFulfillmentDataRequest):
            request = SetAppointmentFulfillmentDataRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ErrorList
        )

    @overload
    def get_range_slot_capacity(
        self, request: GetRangeSlotCapacityRequest, *args, **kwargs
    ) -> ApiResponse[RangeSlotCapacity]:
        """
        Provides capacity slots in a format similar to availability records.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/service/v1/serviceResources/{resourceId}/capacity/range", method="POST"
    )
    def get_range_slot_capacity(
        self, *args, **kwargs
    ) -> ApiResponse[RangeSlotCapacity]:
        """
        Provides capacity slots in a format similar to availability records.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetRangeSlotCapacityRequest):
            request = GetRangeSlotCapacityRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=RangeSlotCapacity
        )

    @overload
    def get_fixed_slot_capacity(
        self, request: GetFixedSlotCapacityRequest, *args, **kwargs
    ) -> ApiResponse[FixedSlotCapacity]:
        """
        Provides capacity in fixed-size slots.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/service/v1/serviceResources/{resourceId}/capacity/fixed", method="POST"
    )
    def get_fixed_slot_capacity(
        self, *args, **kwargs
    ) -> ApiResponse[FixedSlotCapacity]:
        """
        Provides capacity in fixed-size slots.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetFixedSlotCapacityRequest):
            request = GetFixedSlotCapacityRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=FixedSlotCapacity
        )

    @overload
    def update_schedule(
        self, request: UpdateScheduleRequest, *args, **kwargs
    ) -> ApiResponse[UpdateScheduleResponse]:
        """
        Update the schedule of the given resource.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/serviceResources/{resourceId}/schedules", method="PUT")
    def update_schedule(self, *args, **kwargs) -> ApiResponse[UpdateScheduleResponse]:
        """
        Update the schedule of the given resource.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateScheduleRequest):
            request = UpdateScheduleRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=UpdateScheduleResponse
        )

    @overload
    def create_reservation(
        self, request: CreateReservationRequest, *args, **kwargs
    ) -> ApiResponse[CreateReservationResponse]:
        """
        Create a reservation.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/reservation", method="POST")
    def create_reservation(
        self, *args, **kwargs
    ) -> ApiResponse[CreateReservationResponse]:
        """
        Create a reservation.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateReservationRequest):
            request = CreateReservationRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=CreateReservationResponse
        )

    @overload
    def update_reservation(
        self, request: UpdateReservationRequest, *args, **kwargs
    ) -> ApiResponse[UpdateReservationResponse]:
        """
        Update a reservation.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/reservation/{reservationId}", method="PUT")
    def update_reservation(
        self, *args, **kwargs
    ) -> ApiResponse[UpdateReservationResponse]:
        """
        Update a reservation.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateReservationRequest):
            request = UpdateReservationRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=UpdateReservationResponse
        )

    @overload
    def cancel_reservation(
        self, request: CancelReservationRequest, *args, **kwargs
    ) -> ApiResponse[CancelReservationResponse]:
        """
        Cancel a reservation.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/reservation/{reservationId}", method="DELETE")
    def cancel_reservation(
        self, *args, **kwargs
    ) -> ApiResponse[CancelReservationResponse]:
        """
        Cancel a reservation.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CancelReservationRequest):
            request = CancelReservationRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=CancelReservationResponse
        )

    @overload
    def get_appointmment_slots_by_job_id(
        self, request: GetAppointmmentSlotsByJobIdRequest, *args, **kwargs
    ) -> ApiResponse[GetAppointmentSlotsResponse]:
        """
        Gets appointment slots for the service associated with the service job id specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/service/v1/serviceJobs/{serviceJobId}/appointmentSlots", method="GET"
    )
    def get_appointmment_slots_by_job_id(
        self, *args, **kwargs
    ) -> ApiResponse[GetAppointmentSlotsResponse]:
        """
        Gets appointment slots for the service associated with the service job id specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetAppointmmentSlotsByJobIdRequest):
            request = GetAppointmmentSlotsByJobIdRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetAppointmentSlotsResponse,
        )

    @overload
    def get_appointment_slots(
        self, request: GetAppointmentSlotsRequest, *args, **kwargs
    ) -> ApiResponse[GetAppointmentSlotsResponse]:
        """
        Gets appointment slots as per the service context specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           20 |      40 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/appointmentSlots", method="GET")
    def get_appointment_slots(
        self, *args, **kwargs
    ) -> ApiResponse[GetAppointmentSlotsResponse]:
        """
        Gets appointment slots as per the service context specified.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           20 |      40 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetAppointmentSlotsRequest):
            request = GetAppointmentSlotsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetAppointmentSlotsResponse,
        )

    @overload
    def create_service_document_upload_destination(
        self, request: CreateServiceDocumentUploadDestinationRequest, *args, **kwargs
    ) -> ApiResponse[CreateServiceDocumentUploadDestination]:
        """
        Creates an upload destination.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/service/v1/documents", method="POST")
    def create_service_document_upload_destination(
        self, *args, **kwargs
    ) -> ApiResponse[CreateServiceDocumentUploadDestination]:
        """
        Creates an upload destination.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateServiceDocumentUploadDestinationRequest):
            request = CreateServiceDocumentUploadDestinationRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CreateServiceDocumentUploadDestination,
        )
