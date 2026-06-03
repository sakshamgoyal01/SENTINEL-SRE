import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function VerificationTable({
  verifications,
  onSelect,
}: {
  verifications: any[];

  onSelect: (
    verification: any
  ) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>
            Service
          </TableHead>

          <TableHead>
            Result
          </TableHead>

          <TableHead>
            Health
          </TableHead>

          <TableHead>
            Verified
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {verifications.map(
          (
            verification
          ) => (
            <TableRow
              key={
                verification.id
              }
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  verification
                )
              }
            >
              <TableCell>
                {
                  verification.service
                }
              </TableCell>

              <TableCell>
                {
                  verification
                    .verification_result
                }
              </TableCell>

              <TableCell>
                {
                  verification
                    .health_status
                }
              </TableCell>

              <TableCell>
                {
                  verification.verified
                    ? "Yes"
                    : "No"
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}