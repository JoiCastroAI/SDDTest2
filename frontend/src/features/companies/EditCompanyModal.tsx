import React from 'react';
import { Modal, Button } from 'react-bootstrap';
import CompanyForm from './CompanyForm';
import { useUpdateCompanyMutation } from './companiesApi';
import type { Company, CreateCompanyRequest } from '../../types/company';

type EditCompanyModalProps = {
    show: boolean;
    onHide: () => void;
    company: Company | null;
};

const EditCompanyModal: React.FC<EditCompanyModalProps> = ({ show, onHide, company }) => {
    const [updateCompany, { isLoading }] = useUpdateCompanyMutation();

    const handleSubmit = async (data: CreateCompanyRequest) => {
        if (!company) return;
        await updateCompany({ id: company.id, data }).unwrap();
        onHide();
    };

    if (!company) return null;

    return (
        <Modal show={show} onHide={onHide} size="lg" className="company-modal" centered>
            <Modal.Header closeButton>
                <Modal.Title>Edit Company</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <CompanyForm
                    formId="edit-company-form"
                    initialData={company}
                    onSubmit={handleSubmit}
                />
            </Modal.Body>
            <Modal.Footer>
                <Button className="btn-cancel" onClick={onHide}>
                    Cancel
                </Button>
                <Button
                    className="btn-primary-custom"
                    type="submit"
                    form="edit-company-form"
                    disabled={isLoading}
                >
                    {isLoading ? 'Saving...' : 'Save Changes'}
                </Button>
            </Modal.Footer>
        </Modal>
    );
};

export default EditCompanyModal;
