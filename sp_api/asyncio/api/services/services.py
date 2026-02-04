import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class Services(AsyncBaseClient):
    """
    Services SP-API Client
    :link:

    With the Services API, you can build applications that help service providers get and modify their service orders.
    """

    @sp_endpoint("/service/v1/serviceJobs/{}", method="GET")
    async def get_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse:
        """
        get_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse
        
        Gets details of service job indicated by the provided `serviceJobID`.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        20                                      40
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().get_service_job_by_service_job_id("value")
        
        Args:
            serviceJobId: object | required A service job identifier.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), params=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs/{}/cancellations", method="PUT")
    async def cancel_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        cancel_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse
        
        Cancels the service job indicated by the service job identifier specified.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().cancel_service_job_by_service_job_id("value")
        
        Args:
            serviceJobId: object | required An Amazon defined service job identifier.
            key cancellationReasonCode: object | required A cancel reason code that specifies the reason for cancelling a service job.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs/{}/completions", method="PUT")
    async def complete_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        complete_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse
        
        Completes the service job indicated by the service job identifier specified.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().complete_service_job_by_service_job_id("value")
        
        Args:
            serviceJobId: object | required An Amazon defined service job identifier.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs", method="GET")
    async def get_service_jobs(self, **kwargs) -> ApiResponse:
        """
        get_service_jobs(self, **kwargs) -> ApiResponse
        
        Gets service job details for the specified filter query.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      40
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().get_service_jobs()
        
        Args:
            key serviceOrderIds: object |  List of service order ids for the query you want to perform.Max values supported 20.
            key serviceJobStatus: object |  A list of one or more job status by which to filter the list of jobs.
            key pageToken: object |  String returned in the response of your previous request.
            key pageSize: object |  A non-negative integer that indicates the maximum number of jobs to return in the list, Value must be 1 - 20. Default 20.
            key sortField: object |  Sort fields on which you want to sort the output.
            key sortOrder: object |  Sort order for the query you want to perform.
            key createdAfter: object |  A date used for selecting jobs created at or after a specified time. Must be in ISO 8601 format. Required if `LastUpdatedAfter` is not specified. Specifying both `CreatedAfter` and `LastUpdatedAfter` returns an error.
            key createdBefore: object |  A date used for selecting jobs created at or before a specified time. Must be in ISO 8601 format.
            key lastUpdatedAfter: object |  A date used for selecting jobs updated at or after a specified time. Must be in ISO 8601 format. Required if `createdAfter` is not specified. Specifying both `CreatedAfter` and `LastUpdatedAfter` returns an error.
            key lastUpdatedBefore: object |  A date used for selecting jobs updated at or before a specified time. Must be in ISO 8601 format.
            key scheduleStartDate: object |  A date used for filtering jobs schedules at or after a specified time. Must be in ISO 8601 format. Schedule end date should not be earlier than schedule start date.
            key scheduleEndDate: object |  A date used for filtering jobs schedules at or before a specified time. Must be in ISO 8601 format. Schedule end date should not be earlier than schedule start date.
            key marketplaceIds: object | required Used to select jobs that were placed in the specified marketplaces.
            key asins: object |  List of Amazon Standard Identification Numbers (ASIN) of the items. Max values supported is 20.
            key requiredSkills: object |  A defined set of related knowledge, skills, experience, tools, materials, and work processes common to service delivery for a set of products and/or service scenarios. Max values supported is 20.
            key storeIds: object |  List of Amazon-defined identifiers for the region scope. Max values supported is 50.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointments", method="POST")
    async def add_appointment_for_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        add_appointment_for_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse
        
        Adds an appointment to the service job indicated by the service job identifier specified.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().add_appointment_for_service_job_by_service_job_id("value")
        
        Args:
            serviceJobId: object | required An Amazon defined service job identifier.
            body: AddAppointmentRequest | required Add appointment operation input details.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs/{}", method="POST")
    async def reschedule_appointment_for_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        reschedule_appointment_for_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse
        
        Reschedules an appointment for the service job indicated by the service job identifier you specify.
        
        Examples:
            literal blocks::
            
                await Services().reschedule_appointment_for_service_job_by_service_job_id("value")
        
        Args:
            serviceJobId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )






    @sp_endpoint("/service/v1/serviceJobs/{}/appointments/{}", method="POST")
    async def reschedule_appointment_for_service_job_by_service_job_id_post(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse:
        """
        reschedule_appointment_for_service_job_by_service_job_id_post(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse
        
        Reschedules an appointment for the service job indicated by the service job identifier specified.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().reschedule_appointment_for_service_job_by_service_job_id_post("value", "value")
        
        Args:
            serviceJobId: object | required An Amazon defined service job identifier.
            appointmentId: object | required An existing appointment identifier for the Service Job.
            body: RescheduleAppointmentRequest | required Reschedule appointment operation input details.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), serviceJobId, appointmentId), data=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointments/{}/resources", method="PUT")
    async def assign_appointment_resources(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse:
        """
        assign_appointment_resources(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse
        
        Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().assign_appointment_resources("value", "value")
        
        Args:
            serviceJobId: object | required An Amazon-defined service job identifier. Get this value by calling the `getServiceJobs` operation of the Services API.
            appointmentId: object | required An Amazon-defined identifier of active service job appointment.
            body: AssignAppointmentResourcesRequest | required
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), serviceJobId, appointmentId), data=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointments/{}/fulfillment", method="PUT")
    async def set_appointment_fulfillment_data(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse:
        """
        set_appointment_fulfillment_data(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse
        
        Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().set_appointment_fulfillment_data("value", "value")
        
        Args:
            serviceJobId: object | required An Amazon-defined service job identifier. Get this value by calling the `getServiceJobs` operation of the Services API.
            appointmentId: object | required An Amazon-defined identifier of active service job appointment.
            body: SetAppointmentFulfillmentDataRequest | required Appointment fulfillment data collection details.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), serviceJobId, appointmentId), data=kwargs)

    @sp_endpoint("/service/v1/serviceResources/{}/capacity/range", method="POST")
    async def get_range_slot_capacity(self, resourceId, **kwargs) -> ApiResponse:
        """
        get_range_slot_capacity(self, resourceId, **kwargs) -> ApiResponse
        
        Provides capacity slots in a format similar to availability records.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().get_range_slot_capacity("value")
        
        Args:
            resourceId: object | required Resource Identifier.
            body: RangeSlotCapacityQuery | required Request body.
            key marketplaceIds: object | required An identifier for the marketplace in which the resource operates.
            key nextPageToken: object |  Next page token returned in the response of your previous request.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), resourceId), data=kwargs)

    @sp_endpoint("/service/v1/serviceResources/{}/capacity/fixed", method="POST")
    async def get_fixed_slot_capacity(self, resourceId, **kwargs) -> ApiResponse:
        """
        get_fixed_slot_capacity(self, resourceId, **kwargs) -> ApiResponse
        
        Provides capacity in fixed-size slots.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().get_fixed_slot_capacity("value")
        
        Args:
            resourceId: object | required Resource Identifier.
            body: FixedSlotCapacityQuery | required Request body.
            key marketplaceIds: object | required An identifier for the marketplace in which the resource operates.
            key nextPageToken: object |  Next page token returned in the response of your previous request.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), resourceId), data=kwargs)

    @sp_endpoint("/service/v1/serviceResources/{}/schedules", method="PUT")
    async def update_schedule(self, resourceId, **kwargs) -> ApiResponse:
        """
        update_schedule(self, resourceId, **kwargs) -> ApiResponse
        
        Update the schedule of the given resource.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().update_schedule("value")
        
        Args:
            resourceId: object | required Resource (store) Identifier
            body: UpdateScheduleRequest | required Schedule details
            key marketplaceIds: object | required An identifier for the marketplace in which the resource operates.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), resourceId), data=kwargs)

    @sp_endpoint("/service/v1/reservation", method="POST")
    async def create_reservation(self, **kwargs) -> ApiResponse:
        """
        create_reservation(self, **kwargs) -> ApiResponse
        
        Create a reservation.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().create_reservation()
        
        Args:
            body: CreateReservationRequest | required Reservation details
            key marketplaceIds: object | required An identifier for the marketplace in which the resource operates.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/service/v1/reservation/{}", method="PUT")
    async def update_reservation(self, reservationId, **kwargs) -> ApiResponse:
        """
        update_reservation(self, reservationId, **kwargs) -> ApiResponse
        
        Update a reservation.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().update_reservation("value")
        
        Args:
            reservationId: object | required Reservation Identifier
            body: UpdateReservationRequest | required Reservation details
            key marketplaceIds: object | required An identifier for the marketplace in which the resource operates.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), reservationId), data=kwargs)

    @sp_endpoint("/service/v1/reservation/{}", method="DELETE")
    async def cancel_reservation(self, reservationId, **kwargs) -> ApiResponse:
        """
        cancel_reservation(self, reservationId, **kwargs) -> ApiResponse
        
        Cancel a reservation.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().cancel_reservation("value")
        
        Args:
            reservationId: object | required Reservation Identifier
            key marketplaceIds: object | required An identifier for the marketplace in which the resource operates.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), reservationId), params=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointmentSlots", method="GET")
    async def get_appointmment_slots_by_job_id(self, serviceJobId, **kwargs) -> ApiResponse:
        """
        get_appointmment_slots_by_job_id(self, serviceJobId, **kwargs) -> ApiResponse
        
        Gets appointment slots for the service associated with the service job id specified.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().get_appointmment_slots_by_job_id("value")
        
        Args:
            serviceJobId: object | required A service job identifier to retrive appointment slots for associated service.
            key marketplaceIds: object | required An identifier for the marketplace in which the resource operates.
            key startTime: object |  A time from which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `startTime` is provided, `endTime` should also be provided. Default value is as per business configuration.
            key endTime: object |  A time up to which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `endTime` is provided, `startTime` should also be provided. Default value is as per business configuration. Maximum range of appointment slots can be 90 days.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), serviceJobId), params=kwargs)

    @sp_endpoint("/service/v1/appointmentSlots", method="GET")
    async def get_appointment_slots(self, **kwargs) -> ApiResponse:
        """
        get_appointment_slots(self, **kwargs) -> ApiResponse
        
        Gets appointment slots as per the service context specified.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        20                                      40
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().get_appointment_slots()
        
        Args:
            key asin: object | required ASIN associated with the service.
            key storeId: object | required Store identifier defining the region scope to retrive appointment slots.
            key marketplaceIds: object | required An identifier for the marketplace for which appointment slots are queried
            key startTime: object |  A time from which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `startTime` is provided, `endTime` should also be provided. Default value is as per business configuration.
            key endTime: object |  A time up to which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `endTime` is provided, `startTime` should also be provided. Default value is as per business configuration. Maximum range of appointment slots can be 90 days.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/service/v1/documents", method="POST")
    async def create_service_document_upload_destination(self, **kwargs) -> ApiResponse:
        """
        create_service_document_upload_destination(self, **kwargs) -> ApiResponse
        
        Creates an upload destination.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Services().create_service_document_upload_destination()
        
        Args:
            body: ServiceUploadDocument | required Upload document operation input details.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)
