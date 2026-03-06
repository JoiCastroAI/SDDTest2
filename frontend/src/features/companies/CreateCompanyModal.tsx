import React from 'react';
import { Modal, Button } from 'react-bootstrap';
import CompanyForm from './CompanyForm';
import { useCreateCompanyMutation } from './companiesApi';
import type { CreateCompanyRequest } from '../../types/company';

type CreateCompanyModalProps = {
    show: boolean;
    onHide: () => void;
};

const CreateCompanyModal: React.FC<CreateCompanyModalProps> = ({ show, onHide }) => {
    const [createCompany, { isLoading }] = useCreateCompanyMutation();

    const handleSubmit = async (data: CreateCompanyRequest) => {
        await createCompany(data).unwrap();
        onHide();
    };

    return (
        <Modal show={show} onHide={onHide} size="lg" className="company-modal" centered>
            <Modal.Header closeButton>
                <Modal.Title>New Company</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <CompanyForm formId="create-company-form" onSubmit={handleSubmit} />
            </Modal.Body>
            <Modal.Footer>
                <Button className="btn-cancel" onClick={onHide}>
                    Cancel
                </Button>
                <Button
                    className="btn-primary-custom"
                    type="submit"
                    form="create-company-form"
                    disabled={isLoading}
                >
                    {isLoading ? 'Creating...' : 'Create Company'}
                </Button>
            </Modal.Footer>
        </Modal>
    );
};

export default CreateCompanyModal;
